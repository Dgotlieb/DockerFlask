pipeline {
    agent any // You can change 'any' to specify a specific type of agent you want to use
    
    environment {
        DOCKERHUB_CREDS = credentials('docker-hub') // added in Jenkins as docker-hub user/password type
        registry = "${DOCKERHUB_CREDS_USR}" // The name of your user and repository (which can be created manually)
        registryCredential = "${DOCKERHUB_CREDS_PSW}" // The credentials used for your repo added in manage Jenkins
        dockerImage = "" // will be overridden later
    }
    
    stages {
        stage('checkout') {
            steps {
                git(branch: 'main',
                    url: 'https://github.com/raksoq/DockerFlask.git')
            }
        }
        stage('Check Docker Daemon Status') {
            steps {
                sh 'docker version'
            }
        }
        stage('build and push image') {
            
            steps {
                script {
                    echo "Building Docker Image: ${registry}:${BUILD_NUMBER}"
                    dockerImage = docker.build("${registry}:${BUILD_NUMBER}")
                    echo "dockerImage: ${dockerImage}"
                    echo "Pushing Docker Image: ${registry}:${BUILD_NUMBER}"
                    docker.withRegistry("", registryCredential) {
                        dockerImage.push()
                    }
                }

            }
            post {
                always {
                    script {
                        sh "docker image rm -f ${registry}:${BUILD_NUMBER}" // delete the local image if it exists
                    }
                }
            }
        }
    }
}
