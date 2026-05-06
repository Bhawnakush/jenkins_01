pipeline {
    agent any

    environment {
        DOCKERHUB_USER  = 'bhawnakushwaha123'
        IMAGE_NAME      = 'jenkins_prac'
        IMAGE_TAG       = "v${BUILD_NUMBER}"
        FULL_IMAGE      = "${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
        CONTAINER_NAME  = 'my-python-container'
    }

    stages {

        stage('Build Image') {
            steps {
                echo "Building Docker image: ${FULL_IMAGE}"
                sh 'docker build -t ${FULL_IMAGE} .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'bhawnakushwaha123',
                    passwordVariable: 'bhawnakush1208'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${FULL_IMAGE}
                        docker logout
                    '''
                }
            }
        }

        stage('Run Container') {
            steps {
                echo "Stopping and removing any existing container..."
                sh '''
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        ${FULL_IMAGE}
                '''
                echo "Container started: ${CONTAINER_NAME}"
            }
        }

        stage('Verify Python App is Running') {
            steps {
                echo "Waiting for app.py to produce output..."
                sh 'sleep 12'
                sh 'docker logs ${CONTAINER_NAME}'
            }
        }
    }

    post {
        always {
            echo "Cleaning up container..."
            sh 'docker rm -f ${CONTAINER_NAME} || true'
        }
        success {
            echo "Pipeline completed successfully. Image: ${FULL_IMAGE}"
        }
        failure {
            echo "Pipeline failed."
        }
    }
}
