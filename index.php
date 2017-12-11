<?php
  
  $action = 'none';
  $dirname = getcwd();
  $pythonpath = '/usr/local/bin/python3';
  $standup_file = '/tmp/standup.txt';

  if (isset($_POST['start'])) {
    $action = 'start';
    file_put_contents($standup_file, 'started');
  }
  elseif (isset($_POST['continue'])) {
    $action = 'continue';
  }
  elseif (isset($_POST['reset'])) {
    $action = 'reset';

    if (file_exists($standup_file)) {
        unlink('/tmp/standup.txt');
    }
  }

  if ($action !== 'none') {
    shell_exec("{$pythonpath} {$dirname}/standup.py --{$action}-standup > /dev/null 2>&1");
  }

  $started = file_exists($standup_file);

?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>Standup Simulator 2017</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0">

  <style>
    * {
      box-sizing: border-box;
    }

    html,
    body {
      margin: 0;
      padding: 0;
    }

    html {
      font-family: Helvetica, sans-serif;
      font-size: 16px;
    }

    .standup {
      align-items: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    button {
      border-radius: 1rem;
      border: none;
      box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.7);
      color: #FFF;
      font-size: 4.5rem;
      height: calc(40vh - 2rem);
      margin: 1rem;
      padding: 1rem;
      width: calc(100vw - 2rem);
    }

    .start {
      background: green;
    }

    .reset {
      background: blue;
    }

    .continue {
      background: orange;
    }
  </style>
</head>
<body>
  <form class="standup" action="." method="POST">
    <?php if (!$started): ?>
      <button class="start" name="start">Start</button>
    <?php else: ?>
      <button class="continue" name="continue">Continue</button>
    <?php endif; ?>

    <button class="reset" name="reset">Reset</button>
  </form>
</body>
</html>
