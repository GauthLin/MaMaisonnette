<?php
 
// Class qui reprend toutes les infos de la réservation
class info_reservation
{
    private $_chauf1;
    private $_chauf2;
    private $_chauf3;
    private $_lamp;
 
    public function etape1($chauf1, $chauf2, $chauf3)
    {
        $this->_chauf1 = $chauf1;
        $this->_chauf2 = $chauf2;
        $this->_chauf3 = $chauf3;
    }
 
    public function getchauf1()
    {
        return $this->_chauf1;
    }
 
    public function getchauf2()
    {
        return $this->_chauf2;
    }
 
    public function getchauf3()
    {
        return $this->_chauf3;
    }
 
 
    public function getlampe()
    {
        return $this->_lamp;
    }
}