import sys
import ast

def getValueMap(Idict,keys):
    try:
        Odict = ast.literal_eval(Idict)
    except:
        return "Error processing the map"
    
    if(not (isinstance(keys, str))):
        return "Key is not a valid string"

    def get_dict_value(Odict, key):
        return(Odict.get(key))

    for key in keys.split("/"):
        try:
            Odict = get_dict_value(Odict,key)
        except:
            return "Value Not Found in map"
    return "value is : " + str(Odict)

def help():
    print(
        """
        This script will get the value from the map
        Execute the script with 2 argument a map and key
        Example "getValueFromMap.py '{\"x\":{\"y\":{\"z\":\"a\"}}}' "x/y/z"
        """
        )
    sys.exit(1)

if __name__=='__main__':
    try:
        if sys.argv[1] == "-h" : help()
        output = getValueMap(sys.argv[1] ,sys.argv[2])
        print(output)
    except:
        help()
