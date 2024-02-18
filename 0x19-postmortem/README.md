# POSTMORTEM
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
