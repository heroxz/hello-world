pipeline {
   agent any
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
    }
}
