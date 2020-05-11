pipeline {
   agent none
   parameters {
      string(name: 'ESX_BUILD_ID', defaultValue: '00000000', description: '')
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
            }
        }
        stage('Test') {
            steps {
               sh 'node --version'
            }
        }
    }
}
