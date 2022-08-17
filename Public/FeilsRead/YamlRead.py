import  os,yaml,sys

path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),"Config","caseData",'data.yaml')

with open(path,"r",encoding="utf-8") as  f:
    yamlObj=yaml.load(f.read(),Loader=yaml.FullLoader)