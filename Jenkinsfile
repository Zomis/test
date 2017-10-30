

node {
    checkout scm
    def scr = readFile 'resources/jenkins.py'
    println scr.class
    def scr2 = scr.toString().replaceAll('sys.argv[1]', '3')
    println scr2

/*    def script = '''#!/bin/bash

echo $1
'''.trim()*/

//    sh(script: script + "\n423")
    def status = sh(script: scr2, returnStatus: true)
    println "Status result: $status"
}
