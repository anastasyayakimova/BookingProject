pipline{
    agent any

    stages{
        stage('Setup Python Environment'){
            steps{
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'

                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run Tests'){
              steps{
                  sh 'python -m pytest --alluredir allure-results'
              }
        }

        stage('Generate Allure Report'){
                    steps{
                       allure([
                            includeProperties: false,
                            jdk: '',
                            results: [[path: 'allure-results']])
                            ])
                    }
             }
        }

        post{
            always{
                archiveArtifacts artifacts: '**/allure-results/**', allowEmptyArchive^ true
            }
            failure{
                echo 'The build failed'
            }
        }
    }