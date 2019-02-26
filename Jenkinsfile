import groovy.json.JsonSlurper

@Library('ZomisJenkins')
import net.zomis.jenkins.Duga
node {
    //def duga = new Duga()
    //duga.dugaTweet("Jenkins was here")
    println "Test 12345";


    checkout scm
    def scr = readFile 'resources/jenkins.py'
    println scr.class
    println scr.toString().contains('sys.argv[1]')
    def scr2 = scr.toString().replaceAll('sys\\.argv\\[1\\]', '3')
    println scr.equals(scr2)
    println scr2

/*    def script = '''#!/bin/bash

echo $1
'''.trim()*/

//    sh(script: script + "\n423")
    def status = sh(script: scr2, returnStatus: true)
    println "Status result: $status"
}
