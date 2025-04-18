import kue from 'kue';

// Create a queue
const queue = kue.createQueue();

// Define blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
  // Track progress at 0%
  job.progress(0);

  // Check if phoneNumber is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    return done(error);
  }

  // Track progress at 50%
  job.progress(50);

  // Send notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Complete job
  done();
}

// Process jobs with concurrency of 2
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
