pipeline {
   agent none
   environment {
      ESX_BUILD_ID = '00000000'
   }
   stages {
        stage('Build') {
            agent {
               label 'nimbus-worker'
            }
            steps {
                sh 'echo "Hello Jenkins"'
                sh '''
                   echo "Multiline shell steps works too"
                   ls -lah
                '''
                sh 'export esx_build=`/usr/bin/python3 ./getBuildInfo.py`'
                echo '$esx_build'
                withEnv(['ESX_BUILD_ID=`/usr/bin/python3 ./getBuildInfo.py`']) {
                  echo '$ESX_BUILD_ID'
                }
            }
        }
        stage('Test') {
            agent {
               label 'nimbus-worker'
            }
            steps {
               echo "$ESX_BUILD_ID"
            }
        }
    }
}
