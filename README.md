# challengeThree

This script is to process the json object based on the key. 

### Input :
 * Json object
 * Mutiple key path

### Output :
 * The value of the key path in object otherwise error



### Execute with below command :
```sh
  python getValue_Map.py '{\"x\":{\"y\":{\"z\":\"a\"}}}' "x/y/z"
  ```


Sample Input and Output
| Input - Json Object       | Input - Key path | Output - Value |
| ---------------------- | ---------------------- |---------------------- |
| {"x":{"y":{"z":"a"}}}  | x/y/z | a |
| {"x":{"y":{"z":"a"}}}  | x/y | {"z" : "a"} |
| {"a":{"b":{"c":"z"}}}  | a/b/c | z |

### Test case
Added test cases for below scenario
 * Success scenario with key present in object
 * Success scenario without key in object
 * Invalid map input object
 * Invalid key input

### Execute test use below command :
```sh
  python test_getValue_Map.py '{\"x\":{\"y\":{\"z\":\"a\"}}}' "x/y/z"
  ```