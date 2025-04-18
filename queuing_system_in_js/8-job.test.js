import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  // Create a Kue queue in test mode
  before(() => {
    queue = kue.createQueue({ testMode: true });
  });

  // Clear the queue after each test
  afterEach(() => {
    queue.testMode.clear();
  });

  // Exit test mode after all tests
  after(() => {
    queue.testMode.exit();
  });

  // Test case: jobs is not an array
  it('display a error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  // Test case: create two new jobs to the queue
  it('create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Verify two jobs were created
    expect(queue.testMode.jobs.length).to.equal(2);

    // Verify job types
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');

    // Verify job data
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});