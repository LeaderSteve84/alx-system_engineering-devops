# 0x19. Postmortem
### DevOps SysAdmin
 <p>By: Sylvain Kalache<br />
 Weight: 1<br />
 Project over - took place from Feb 12, 2024 6:00 AM to Feb 19, 2024 6:00 AM<br />
 Manual QA review was done by Hauwa Abdulkadir on Feb 18, 2024 1:41 PM<br />
</P>
<article>
<h2>Concepts</h2>
<p>For this project, we expect you to look at this concept:
<br /><br />
<li>On-call</li>
</article>
<article>
<h3>Background Context</h3>

<p>
Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.
<br /><br />
A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:<br />
<br /><br />
<li>To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.</li>
<li>And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.</li>
</p>
</article>
<article>
<h2>Resources</h2>
<p>Read or watch:
<ul>
<li><a href="https://sysadmincasts.com/episodes/20-how-to-write-an-incident-report-postmortem">Incident Report, also referred to as a Postmortem</a></li>
<li><a href="https://www.atlassian.com/incident-management/postmortem">The importance of an incident postmortem process</a></li>
<li><a href="https://www.pagerduty.com/resources/learn/incident-postmortem/">What is an Incident Postmortem?</a></li>
</p>
<article>
<h4>More Info</h4>
<p>
Manual QA Review<br />
It is your responsibility to request a review for your postmortem from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.
</p>
</article>
</article>
<article>
<hgroup>
<h1> Tasks </h1>
<h3>0. My first postmortem</h3>
</hgroup>
<p>mandatory</p>

<p>
Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)
<br />
<br />
Requirements:
<div>
Issue Summary (that is often what executives will read) must contain:
duration of the outage with start and end times (including timezone)
what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
what was the root cause
Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:
</div>
<div>
when was the issue detected
how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
misleading investigation/debugging paths that were taken
which team/individuals was the incident escalated to
how the incident was resolved
Root cause and resolution must contain:
</div>
<div>
explain in detail what was causing the issue
explain in detail how the issue was fixed
Corrective and preventative measures must contain:
</div>
<div>
what are the things that can be improved/fixed (broadly speaking)
a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)
Be brief and straight to the point, between 400 to 600 words
<br />
While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.
<br />
Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.
</div>
</article>

<h2>POSTMORTEM</h2>
<p>
The incidence report for an Apache outage that occured on Feb 17, 2024.<br /> 
We apologize to everyone who was affected.<br />
</p>
<article>
  <header>
   <h2>ISSUE SUMMARY</h2>
  </header>
  <div>
	On Sat 17, Feb 2024, 08:01 GMT, our Apache Server return 500 internal<br />
 	server error. The error lasted for 3 hours before it was resolved. 100% of <br />
	traffic to our website were not able to access the http response. The root<br />
	cause of the problem, was as a result of a typo error in the configuration setting file.<br />
	Instead of "php" string, it was typed as "phpp" string. 
  </div>
</article>
<article>
  <header>
   <h2>TIMELINE</h2>
  </header>
  <div>
   <ul>
   <li>09:00 GMT: issue detected</li>
   <li>08:55 GMT: datadog detected the issue</li>
   <li>09:15 GMT: checking if the servers were running and if an issue with the servers networking</li>
   <li>09:45 GMT: the issue was escalated to the software engineering team</li>
   <li>10:15 GMT: the typo error ("phpp") was detected and corrected to "php"</li>
   <li>10:20 GMT: 100% of traffic back online</li>
   </ul>
  </div>
</article>
<article>
  <header>
   <h2>ROOT CAUSE AND RESOLUTION</h2>
  </header>
  <div>
   <p>A configuration change was released into our production environment at 08:01 GMT.<br />
        This configuration was not released to our testing environment before released to<br />
        production. Therefore a string error caused an internal server error. 100% of<br />
	traffic could not accessed the site. At 08:55 GMT, the monitoring system detected<br />
        the incidence and alerted the on-call engineer who investigated and escalated the<br />
	issue to the software engineering team.
   </p>
   <p>After several investigation, using tmux and strace. It was discoverd that a<br />
       typo error in the configuration file was ressponsible for the error. Therefore,<br />
       the error was corrected at 10:15 GMT and 100% traffic were restored back to the website.
   </p>
  </div>
</article>
<article>
  <header>
   <h2>CORRECTION AND PREVENTIVE MEASURES</h2>
  </header>
  <div>
	This incidence occured because the configuraton change was not tested before it was deployed.<br /> 
	To avoid future reoccurence of this incidence. Every modification of configuration settings<br />
	must be properly tested in our testing environment before deploying to our production environment.<br />
  </div>
</article>
