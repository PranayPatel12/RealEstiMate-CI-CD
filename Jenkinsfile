pipeline {
    agent any

    environment {
        IMAGE_NAME = 'realestimate-image'
        DOCKERHUB_IMAGE = 'pranay590/realestimate-image:latest'
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

        stage('Install Dependencies') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'No tests defined. Skipping...'
                // Add your test commands like pytest here if needed
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Tag and Push to DockerHub') {
            steps {
                withCredentials([string(credentialsId: 'Docker-hub-credentials', variable: 'DOCKER_HUB_PASS')]) {
                    sh """
                        echo "$DOCKER_HUB_PASS" | docker login -u pranay590 --password-stdin
                        docker tag $IMAGE_NAME $DOCKERHUB_IMAGE
                        docker push $DOCKERHUB_IMAGE
                    """
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME -p $HOST_PORT:$CONTAINER_PORT $IMAGE_NAME
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
