pipeline {
   agent {
      docker {image 'node:7-alpine' }
   }
   stages {
        stage('Build') {
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
