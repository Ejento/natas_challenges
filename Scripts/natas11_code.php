<?php
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
function xor_encrypt($in, $key) {
    $text = $in;
    $outText = '';
    for($i=0;$i<strlen($text);$i++) {
    	$outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
    return $outText;
}

$plaintext = json_encode($defaultdata);

// The ciphertext is what I found in my cookie
$ciphertext = hex2bin("0a554b221e00482b02044f2503131a70531957685d555a2d121854250355026852115e2c17115e680c");

// If we encrypt the plaintext with the ciphertext we are gonna get the key back.
// And as you can see the key repeats some time because the string was bigger than the key, but we need it only one time.
echo(xor_encrypt($plaintext, $ciphertext));

$key = "qw8J";
$good_data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
$good_plaintext = json_encode($good_data);
$good_ciphertext = xor_encrypt($good_plaintext, $key);

// The encrypted data that we can use
echo(base64_encode($good_ciphertext));

?>