## Monthly Cost Analysis
Region: East Asia

| Azure Resource | Service Tier | Monthly Cost |
| ------------ | ------------ | ------------ |
| *Azure Postgres Database* |   Basic, 2 vCore(s), 5 GB  |       95.44 USD       |
| *Azure Service Bus*   |    Basic     |       	$0.05 per million operations       |
| *Azure App Service Plan for Web App*   |     F1    |     Free         |
| *Azure App Service Plan for Function*   |     Consumption    |     $0.20 per million executions, 1 million executions         |

## Architecture Explanation
This is a placeholder section where you can provide an explanation and reasoning for your architecture selection for both the Azure Web App and Azure Function.

- For the Azure Web App, I choose the Free Plan (F1) because the recent application does not require high performance or any advanced needs. With the F1 plan, it provides enough resource (1GB RAM, 1GB Storage) for the application.
- For the Azure Function, I choose the  Consumption plan pricing because it includes a monthly free grant of 1 million requests and 400,000 GB-s of resource consumption per month per subscription in pay-as-you-go pricing across all function apps in that subscription. The recent function performs simple task, it does not require high performance, so I don't need to upgrade to the Premium plan.
