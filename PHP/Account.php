<?php
class Account {
    public $id;
    public $name;
    public $document;
    public $mail;
    public $password;

    public function __construct($name, $document, $mail, $password)
    {
        $this->name = $name;
        $this->document = $document;
        $this->mail = $mail;
        $this->password = $password;
    }
}