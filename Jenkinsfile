

node {
    checkout scm
    def scr = readFile 'resources/jenkins.py'
    println scr
    scr = scr.replaceAll('sys.argv[1]', 3)

/*    def script = '''#!/bin/bash

echo $1
'''.trim()*/

//    sh(script: script + "\n423")
    sh scr
}
