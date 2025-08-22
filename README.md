## Cherry Leaf Powdery Mildew Detector

# ![Cherry leaf](streamlit_images/cherry-leaf.png)

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
- The dataset contains 4208 images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Hypotheses and validation

- List here your project hypothesis(es) and how you envision validating it (them).

- **Hypothesis 1:** There is a noticeable visual difference between healthy cherry leaves and those infected with powdery mildew. This difference can be observed in features like texture, colour, and the presence of white, powdery spots.

- **Validation 1:** The hypothesis was tested using image montages, average images, variability images and by studying the differences.

- **Hypothesis 2:** A machine learning model can be trained to accurately classify cherry leaves as either healthy or infected, achieving an accuracy of 97% or higher.

- **Validation 2:** The hypothesis was tested by splitting the data into Training, Validation and Test sets, training the Convolutional Neural Network (CNN) on the training and validation sets and then using the test set to make predictions.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

The project followed a CRISP-DM workflow in order to effectively map the business requirements with the machine learning tasks.

**Business requirement 1: Data visualisation**

The first requirement is a foundational step in any data sciencce project: esploratory data analysis (EDA). Before building a predictive model, it's crucial to understand the characteristics of the data. Analysing the average images, variability images, and creating an image montage for each class directly fulfills this need.

- Average and Variability Images: These visualisation provide statistical insights into the dataset. The average images for healthy and posdery mildew leaves show the typical appearance of each class, showing the most common feature and colour patterns. In contrast, the variability images highlight areas of high pixel value variance, indicating where leaves are most diverse or where the disease manifests with different patterns. These visualisations help identify the key visual features that will likely be most useful for the model to learn.

- Image montage: A montage provides a qualitative overview of the dataset. It helps to visually inspect the variety of images, check for potential data quality issues (e.g., poor lighting or mislabelled images), and confirm that the dataset is representative of the real-world problem. This step validates the data's suitability for the project.

These tasks are essential for the data understanding phase of the CRISP-DM workflow, providing the necessary insights to inform the subsequent data preparation and modelling stages.

**Business requirement 2: Predictive ML system**

This requirement directly maps to a machine learning classification task. The goal is to build a system that can take an image as input and predict its class (healthy or powdery mildew). This is a classica binary image classification problem.

- Neural networks: The suggestion to use neural networks, specifically convolutional neural networks (CNN), is the industry-standard approach for image classification. CNNs are adept at learning hierarchical features from raw pixel data, making them ideal for this task. They can automatically identify complex patterns, such as the unique spots and textures associated with posdery midlew, without the need for manual feature engineering.

- Image resizing anf model size: The recommendation to use a smaller image size (e.g., 50x50 or 100x100) is a practival constraint related to model deployment and management. A smaller input size leads to a smaller model with fewer paramenters, which is easier to share, store on platfoms like GitHub, and deploy. This decision involves a trade-off: a smaller size might lead to a slight loss in detail, potentially impacting accuracy. The task, therefore, is about finding the optimal image size that meets the performance requirements while staying within the model size constraint. This strategic consideration is a key part of the data preparation and modeling phases, ensuring the final product is not only accurate but also practical for real-world use.

## ML Business Case

- In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

## Dashboard Design

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- The repository template used for this project was created by Code Institute.
- Code from Code Institute's Walk through Project 01 has been used on the Data collection, Data visualisation and Modelling Evaluating jupyter notebooks.
- Inspiration and code have been used and adapted from cla-cif's Cherry-Powdery-Mildew-Detector project [https://github.com/cla-cif/Cherry-Powdery-Mildew-Detector] and barty-s' cherry-leaf-mildew-detection project [https://github.com/barty-s/cherry-leaf-mildew-detection-project] for the Data collection, Data visualisation and Modelling Evaluating jupyter notebooks.
- Definition of cherry powdery mildew was adapted from the Washington State University website [https://treefruit.wsu.edu/crop-protection/disease-management/cherry-powdery-mildew/].
- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.
