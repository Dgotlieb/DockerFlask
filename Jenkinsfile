pipeline {
    environment {
    DOCKERHUB_CREDS = credentials('docker-hub') // added in Jenkins as docker-hub user/password type
    registry = ${DOCKERHUB_CREDS_USR} // The name of your user and repository (which can be created manually)
    registryCredential = ${DOCKERHUB_CREDS_PSW} // The credentials used to your repo added in manage jenkins
    dockerImage = "" // will be overridden later
  }
    stages{
        stage('checkout') {
            steps {
                git (branch: 'main',
                     url: 'https://github.com/raksoq/DockerFlask.git')
            }
        }
        stage('build and push image') {
                steps {
                   script {
                        dockerImage = docker.build registry + ":$BUILD_NUMBER“ // give a name and version to image
                        docker.withRegistry('', registryCredential) {
                        dockerImage.push() // push image to hub
                    }
                }
            }
        }
    
         post {
         always {
             script{
                 sh 'docker rmi $registry:$BUILD_NUMBER' // delete the local image at the end
             }
    
         }
         }
    }
