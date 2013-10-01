<html>
	<head>
		<link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.3.0/pure-min.css">
	</head>
	
	<body>

	
		<div id="fb-root"></div>
			<script>
			  window.fbAsyncInit = function() {
			  FB.init({
			    appId      : '657737804244482', // App ID
			    channelUrl : '//lit-harbor-9828.herokuapp.com/channel.html', // Channel File
			    status     : true, // check login status
			    cookie     : true, // enable cookies to allow the server to access the session
			    xfbml      : true  // parse XFBML
			  });

			 
			  FB.Event.subscribe('auth.authResponseChange', function(response) {
			    if (response.status === 'connected') {
			      testAPI();
			    } else if (response.status === 'not_authorized') {
			      FB.login();
			    } else {
			      FB.login();
			    }
			  });
			  };

			  // Load the SDK asynchronously
			  (function(d){
			   var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
			   if (d.getElementById(id)) {return;}
			   js = d.createElement('script'); js.id = id; js.async = true;
			   js.src = "//connect.facebook.net/en_US/all.js";
			   ref.parentNode.insertBefore(js, ref);
			  }(document));

			  // Here we run a very simple test of the Graph API after login is successful. 
			  // This testAPI() function is only called in those cases. 
			  function testAPI() {
			    console.log('Welcome!  Fetching your information.... ');
			    FB.api('/me', function(response) {
			      console.log('Good to see you, ' + response.name + '.');
			    });



			    function showFriends(){

			    };
			  };

			</script>

	<!-- Login -->
	<h1> Friends in Far Places </h1>
	<p> When traveling let friends be your guide </p>

	<?php

			/* ASSIGN MY FACEBOOK  */
			/* Note: this will not work unless you get your own access token from: https://developers.facebook.com/tools/explorer/    */
			$graph_url = file_get_contents('https://graph.facebook.com/4202803?fields=friends&access_token=CAAJWNYQtZAgIBAIlrIZCZB4xwRrZAhLt97lnNnOAG6S61yzWNIB2i8dujzncZCidDcqxiv59tYm5GQ7dWjEVUB8a8zYFjTXZCciWRqrAdBlZCsSJqcmi5kSceTTt4M6ONrRh17W9AvznhZAbIjeQ1BwE1tpZAb1ZCES9lNCsndaDNEPYhx1DJjCgs0qFLsvqAaePl3fYqgjp6RsAZDZD');
			
			$graph_output = json_decode($graph_url);

			/* TESTING TO SEE THE DATA */
			// echo "<pre>";
			// print_r($graph_output);
			// echo "</pre>";
			
			/* PRINT OUT RESULTS */
			
			echo $graph_output->friends
			
		
			
		?>
	<fb:login-button autologoutlink="true" width="400" max-rows="1"></fb:login-button></a>
	
	

	

	</body>
</html>