t request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);

    // Initialize an object to store the count of completed tasks per user
    const completedTasksCount = {};

    // Loop through all the todos
    for (const todo of todos) {
      // Check if the task is completed (completed is true)
      if (todo.completed) {
        // Increment the count for the corresponding userId
        if (completedTasksCount[todo.userId]) {
          completedTasksCount[todo.userId]++;
        } else {
          completedTasksCount[todo.userId] = 1;
        }
      }
    }

    // Print the results
    console.log(completedTasksCount);
  }
});
