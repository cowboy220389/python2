This will be my fist web application!
It takes a dataset, vehicles_us.csv, and compares price by model year(to see how vehicles depreciate)
It then compares odometer by price to (to see how miles affect depreciation)
The code is refactored from triple ten's blog post. It uses packages: pandas, plotly.express, and streamlit. The methods used are: st.header,
st.dataframe, st.write, px.scatter, and px.histogram.

Here is the url of my app on render: https://dashboard.render.com/web/srv-cpsqqn08fa8c739d7nc0/deploys/dep-cpsqqn88fa8c739d7ngg
It is still a work in progress as I do not know how to fix the last data visulization(the one that the user can change the parameter of), it also used the original dataset without my changes, which i will update
when I find out how.

The code to write a similar application is on tripleten's blog post, here:https://www.tripleten.blog/posts/deploying-data-science-web-apps-to-the-cloud, as well as on Github here:https://github.com/alex000kim/simple-streamlit-datavis-app/blob/main/app.py
