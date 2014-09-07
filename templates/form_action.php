 <html>
    <head>
        <title>Handle POST requests with Flask</title>
        <link rel=stylesheet type=text/css href="{{ url_for('static', 
        filename='style.css') }}">
    </head>
    <?php
    $name = {{name}};
    $email = $_POST['youremail'];

    print "name is $name";
    print "email is $email";
    ?>

    <body onload="test({{name}})">
        <div id="container">
            <div class="title">
                <h1>POST request with Flask</h1>
            </div>
            <div id="content">
                Hello <strong>{{name}}</strong> ({{email}})!
                Welcome {{name}}<?php echo $name; ?><br>
Your email address is: <?php echo $_POST["youremail"]; ?>

            </div>
            <div class="title">
                <h1 id="flask_code">Flask code</h1>
            </div>
                <code><pre>
@app.route('/hello/', methods=['POST'])
def hello():
    name=request.form['yourname']
    email=request.form['youremail']
    return render_template('form_action.html', name=name, email=email)
                </pre></code>
            </div>
        </div>
    </body>

    <script type="text/javascript">
    function test(string){

        //console.log("Reached form_action.html")
        document.getElementById("flask_code").innerHTML = string;
    }

    </script>
</html>