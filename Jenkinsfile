pipeline {
    agent any

    environment {
        IMAGE_NAME = 'realestimate-image'
        DOCKERHUB_USERNAME = 'pranay590'
        DOCKERHUB_IMAGE = "${DOCKERHUB_USERNAME}/realestimate-image:latest"
        CONTAINER_NAME = 'realestimate-container'
        HOST_PORT = '8000'
        CONTAINER_PORT = '8000'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/PranayPatel12/RealEstiMate-CI-CD.git', branch: 'main'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'No tests defined. Skipping...'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Tag and Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh """
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker tag $IMAGE_NAME $DOCKER_USERNAME/$IMAGE_NAME:latest
                        docker push $DOCKER_USERNAME/$IMAGE_NAME:latest
                    """
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME -p $HOST_PORT:$CONTAINER_PORT $DOCKERHUB_USERNAME/$IMAGE_NAME:latest
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed!'
        }
    }
}
