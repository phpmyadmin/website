<?php
if (isset($$_GET['issue'])) {
    header("Location: ${server}${base_url}security/" . $$_GET['issue'] . "${file_ext}");
} else {
    header("Location: ${server}${base_url}security/");
}
?>
