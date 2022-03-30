## Monthly Cost Analysis
Region: East Asia

| Azure Resource | Service Tier | Monthly Cost |
| ------------ | ------------ | ------------ |
| *Azure Postgres Database* |   Basic, 2 vCore(s), 5 GB  |       95.44 USD       |
| *Azure Service Bus*   |    Basic     |       	$0.05 per million operations       |
| *Azure App Service Plan for Web App*   |     F1    |     Free         |
| *Azure App Service Plan for Function*   |     Consumption    |     $0.20 per million executions, 1 million executions         |
| *Storage account*   |     General Purpose V2    |     $123.92         |
| *Sendgrid*   |     Free    |     Free         |

In terms of an enterprise level application deployed on production, I would keep all things the same, except:
| Azure Resource | Service Tier | Monthly Cost |
| ------------ | ------------ | ------------ |
| *Azure App Service Plan for Web App*   |     B1    |     $14.60         |
| *Sendgrid*   |     Pro    |     $89.95         |

Because when we deploy to production, I think we need more resource to serve customers.

## Architecture Explanation
This is a placeholder section where you can provide an explanation and reasoning for your architecture selection for both the Azure Web App and Azure Function.

- For the Azure Web App, I choose the Free Plan (F1) because the recent application does not require high performance or any advanced needs. With the F1 plan, it provides enough resource (1GB RAM, 1GB Storage) for the application. 
    - Cost-effectiveness: We can share the same App Service Plan with Azure Function to reduce the cost.
    - Advantages:
        - Multiple languages and frameworks supported: ASP.NET, ASP.NET Core, Java, Ruby, Node.js, PHP, or Python...
        - Global scale with high availability: Scale up or out manually or automatically.
        - Infrastructure is managed by Azure, so we can focus on business logic.
    - How this architecture removes the flaws of the traditional app deployed on-premise in terms of scalability and handling timeout exceptions:
        - Scalability: On-premise can hamper your business growth due to a lack of scalability. Updates usually require modifications to software and hardware. With Azure Web App service, we can scale up (Get more CPU, memory, disk space...) or scale out (increase the number of VM instances that run your app) by change the pricing tier of App Service Plan and it cost less than update hardware.
- For the Azure Function, I choose the  Consumption plan pricing because it includes a monthly free grant of 1 million requests and 400,000 GB-s of resource consumption per month per subscription in pay-as-you-go pricing across all function apps in that subscription. The recent function performs simple task, it does not require high performance, so I don't need to upgrade to the Premium plan.
    - Cost-effectiveness: Only pay for the computing resources based on the number of executions, time of execution, and memory used
    - Advantages:
        - Scales automatically, even during periods of high load. Azure Functions infrastructure scales CPU and memory resources by adding additional instances of the Functions host, based on the number of incoming trigger events.
        - Be charged for compute resources only when functions are running.
        - Execution times out after a configurable period of time.
        - Azure Functions can be hosted on the same App Service plan as web app.
        - Configure the timeout or handle long-time HTTP request.
    - How this architecture removes the flaws of the traditional app deployed on-premise in terms of scalability and handling timeout exceptions:
        - Scalability: Automatically.
        - Avoid long running functions: a function execution times out after a configurable period of time.  For example, a webhook or HTTP trigger function might require an acknowledgment response within a certain time limit; it's common for webhooks to require an immediate response. You can pass the HTTP trigger payload into a queue to be processed by a queue trigger function.
