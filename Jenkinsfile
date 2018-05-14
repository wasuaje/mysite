node{

   stage('Check Out') {
    checkout scm
    }

    stage('Build') {
      echo "Building project"
      sh  "docker build --rm -t testing:latest ."

    }

    stage('Test') {

      echo "Running Tests"
      sh '''docker run testing:latest ./test
 
      if [ $? -ne 0 ]; then
              echo "Tests did not pass! Fix it."
              exit 1
      fi
       
          '''
    }

    stage('Stop Services') {
      echo "Stopping Services"
      sh  "/usr/local/bin/docker-compose down"
    }

    stage('Building Static Site') {
      echo "Building Static Site"
      sh "docker run -v ${pwd}/static-site:/nikola dragas/nikola:alpine sh static-site-build"
    }

    stage('Start Services') {
      echo "Starting project"
      sh  "/usr/local/bin/docker-compose up -d"
    }

    stage('Print Logs') {
      echo "Printing logs."
      sh  '''/usr/local/bin/docker-compose logs --tail="all" '''

    }

  }

