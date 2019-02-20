# Page parts

header = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Locky</title>
    <link rel="stylesheet" type="text/css" href="/style/style.css">
    <link rel="stylesheet" type="text/css" href="/style/bootstrap-grid.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    <link rel="shortcut icon" href="/favicon.ico">
</head>
"""

navbar = """
<nav class="navbar navbar-default">
        <div class="container-fluid">
      <a id="locky" class="navbar-brand" href="#"><span class="glyphicon glyphicon-lock"></span> Locky</a>
    <ul class="nav navbar-nav">
      <li class="active"><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Feaches</a></li>
      <li><a href="/control">Control</a></li>
    </ul>
    <ul class="nav navbar-nav navbar-right">
      <li><a href="#"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
      <li><a href="/login"><span class="glyphicon glyphicon-log-in"></span> Login</a></li>
    </ul>
        </div>
    </nav>
"""

content = """
    <div class="main container vert-offset-bottom-1">
        <h1>RFID-Lock</h1>
    </div>
"""

form = """
    <form method="post" class="form-horizontal offset-sm-2 vert-offset-top-2" action="control">
        <div class="form-group">
            <label class="control-label col-sm-2" for="username">Username:</label>
            <div class="col-sm-6">
                <input type="text" class="form-control" id="username" name="username">
            </div>
        </div>
        <div class="form-group">
            <label class="control-label col-sm-2" for="password">Password:</label>
            <div class="col-sm-6">
                <input type="password" class="form-control" id="password" name="password">
            </div>
        </div>

        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
                <button type="submit" class="btn btn-default">Sign in</button>
            </div>
        </div>
    </form>
"""
