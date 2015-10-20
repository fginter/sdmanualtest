import sys
import glob
import os.path
import json
import re
import codecs
import StringIO
import subprocess

valueRe=re.compile(u"^([a-zA-Z ]+): ([A-Za-z0-9+. -]+)$")
def analyze_readme(dir_name):
    readme_data={u"Documentation status":u"stub",u"Data source":u"automatic conversion",u"License":u"none",u"Data available since":u"none"}
    readmes=sorted(x for x in glob.glob(os.path.join(dir_name,"*")) if "readme" in x.lower())
    if not readmes: #No readme file!
        return readme_data
    with codecs.open(readmes[0],"r","utf-8") as f:
        for line in f:
            match=valueRe.match(line)
            if match: #Maybe one of our values?
                cat,val=match.groups()
                if cat in readme_data:
                    #Yes! this is a known category, we have a perfect match
                    readme_data[cat]=val
    return readme_data
                
def get_language_span(l):
    return """<span class="doublewidespan" style="padding-left:3em">{}</span>""".format(l.replace(u"_",u" "))

def get_wide_span(l):
    return """<span class="widespan">{}</span>""".format(l.replace(u"_",u" "))


def run_validation(l,args):
    outp=""
    validates=True
    files=sorted(glob.glob(os.path.join(args.ud_data,"UD_"+l,"*.conllu")))
    if not files:
        return False, "No data"
    for f in files:
        cmd=["python",os.path.join(args.ud_tools,"validate.py"),"--lang",lcodes[l],f]
        outp+=" ".join(cmd)
        p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out,err=p.communicate()
        if out==None:
            out=""
        if err==None:
            err=""
        if p.returncode!=0:
            validates=False
        outp+=out
        outp+="\n\n"
        outp+=err
        outp+="\n\n******************\n\n"
    return validates,outp


lcodes=json.loads(open("lcodes.json").read())
def gen_table(args):
    
    a_data=StringIO.StringIO()
    print >> a_data, "<!-- content of _includes/at_glance.html -->"
    print >> a_data, "<!-- do NOT edit by hand, that file is autogenerated using gen_index/index_page.py -->"
    # Will create a line for every language which has a repository
    langs=sorted(os.path.basename(x).replace(".json","") for x in glob.glob("_corpus_data/*.json"))
    for l in langs:
        print >> sys.stderr, "Validation run for", l
#    for l in "Finnish","English","Ancient_Greek":
        readme_data=analyze_readme(os.path.join(args.ud_data,"UD_"+l))
        if readme_data.get("Data available since") not in ("UD v1.0","UD v1.1","UD v1.2"):
            continue #Skip this language
        validates,val_output=run_validation(l,args)
        print >> a_data, "<div>"
        print >> a_data, get_language_span(l)
        print >> a_data, get_wide_span(lcodes[l])
        if validates:
            print >> a_data, """<span class="validationpass">PASS</span>"""
        else:
            if val_output=="No data":
                print >> a_data, """<span class="validationfail">NO DATA</span>"""
            else:
                print >> a_data, """<span class="validationfail">FAIL</span>"""
        print >> a_data, "</div>"

        print >> a_data, "<div>"
        print >> a_data, "<pre>"
        print >> a_data, val_output
        print >> a_data, "</pre>"
        print >> a_data, "</div>"
    return a_data



if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='generates the index page')
    parser.add_argument('--ud-data', required=True, help='Where is the UD data, so I can grab the readmes? (DIRECTORY)')
    parser.add_argument('--ud-tools', required=True, help='Where is the UD tools? (DIRECTORY)')
    args = parser.parse_args()
    
    a_data=gen_table(args)
    print a_data.getvalue()
