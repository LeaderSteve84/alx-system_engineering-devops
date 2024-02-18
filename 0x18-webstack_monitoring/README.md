<article>
<hgroup>
 <h1>0x18. Webstack monitoring</h1>
 <h3>DevOps SysAdmin monitoring</h3>
</hgroup>
<h3>Background Context</h3>

<p>
“You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.
</p>
<p>
Web stack monitoring can be broken down into 2 categories:
</p>
<p>
Application monitoring: getting data about your running software and making sure it is behaving as expected
Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)
</p>
<p>
Resources
Read or watch:
</p>
<p>
<ul>
<li><a href="">What is server monitoring</a></li>
<li><a href="">What is application monitoring</a></li>
<li><a href="">System monitoring by Google</a></li>
<li><a href="">Nginx logging and monitoring</a></li>
</ul>
<h2>Learning Objectives</h2>
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
</p>
<h3>General</h3>
<p>
<li>Why is monitoring needed</li>
<li>What are the 2 main area of monitoring</li>
<li>What are access logs for a web server (such as Nginx)</li>
<li>What are error logs for a web server (such as Nginx)</li>
<li>Copyright - Plagiarism</li>
<li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
<li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.</li>
<li>You are not allowed to publish any content of this project.</li>
<li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
</p>
<h3>Requirements</h3>
<h4>General</h4>
<p>
<li>Allowed editors: vi, vim, emacs</li>
<li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A README.md file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass Shellcheck (version 0.3.7) without any error</li>
<li>The first line of all your Bash scripts should be exactly #!/usr/bin/env bash</li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</p>
<br />
<h4>Your servers</h4>
<table cellspacing=4>
  <thead>
   <tr>
   <th>Name</th>
   <th>Username</th>
   <th>IP</th>
   <th>State</th>
   </tr>
  </thead>
  <tbody>
   <tr>
   <td>430xxx-web-01</td>
   <td>xxxxxx</td>
   <td>54.167.187.xxx</td>
   <td>running</td>
   </tr>
   <tr>
   <td>430xxx-web-02</td>	
   <td>xxxxxx</td>
   <td>100.25.3.xxx</td>	
   <td>running</td>	
   </tr>
   <tr>
   <td>430xxx-lb-01</td>	
   <td>xxxxxx</td>	
   <td>34.239.254.xxx</td>
   <td>running</td>	
   </tr>
  </tbody>
</table>
</article>
<article>
<h1>Tasks</h1>
<p>
<h4>0. Sign up for Datadog and install datadog-agent</h4>
<h5>mandatory</h5>
</p>
<p>
For this task head to https://www.datadoghq.com/ and sign up for a free Datadog account. When signing up, you’ll have the option of selecting statistics from your current stack that Datadog can monitor for you. Once you have an account set up, follow the instructions given on the website to install the Datadog agent.
</p>
<p>
<ul>
<li>Sign up for Datadog - Please make sure you are using the US website of Datagog (https://app.datadoghq.com)</li>
<li>Use the US1 region</li>
<li>Install datadog-agent on web-01</li>
<li>Create an application key</li>
<li>Copy-paste in your Intranet user profile (here) your DataDog API key and your DataDog application key.</li>
<li>Your server web-01 should be visible in Datadog under the host name XX-web-01</li>
 <ul>
 <li>You can validate it by using this API</li>
 <li>If needed, you will need to update the hostname of your server</li>
 </ul>
</ul>
</p>

<h4>Repo:</h4>

<li>GitHub repository: alx-system_engineering-devops</li>
<li>Directory: 0x18-webstack_monitoring</li>
     
<p>

<h4>1. Monitor some metrics</h4>
<h5>mandatory</h5>
Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some monitors within the Datadog dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: System Check.
</p>
<p>
Set up a monitor that checks the number of read requests issued to the device per second.
Set up a monitor that checks the number of write requests issued to the device per second.
</p>

<h4>Repo:</h4>
<p>
<li>GitHub repository: alx-system_engineering-devops</li>
<li>Directory: 0x18-webstack_monitoring</li>
</p> 

<h4>2. Create a dashboard</h4>
<h5>mandatory</h5>
<p>
Now create a dashboard with different metrics displayed in order to get a few different visualizations.
</p>
<p>
Create a new dashboard
Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever you’d like
Create the answer file 2-setup_datadog which has the dashboard_id on the first line. Note: in order to get the id of your dashboard, you may need to use Datadog’s API
</p>
<h5>Repo:</h5>
<p>
<li>GitHub repository: alx-system_engineering-devops</li>
<li>Directory: 0x18-webstack_monitoring</li>
<li>File: 2-setup_datadog</li>
</p>
