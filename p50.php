<?php

/*
 * https://projecteuler.net/problem=50
 *
 * The prime 41, can be written as the sum of six consecutive primes:
 *
 * 41 = 2 + 3 + 5 + 7 + 11 + 13
 * This is the longest sum of consecutive primes that adds to a prime below one-hundred.
 *
 * The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
 *
 * Which prime, below one-million, can be written as the sum of the most consecutive primes?
 */
class P50
{
    public $limit = 1000000;
    public $max;
    public $primeList;

    public function isPrime($n)
    {
        for ($x = 2; $x < 0.5 * $n; $x ++) {
            if ($n % $x == 0) {
                return FALSE;
            }
        }
        return TRUE;
    }

    public function genNextPrime($n)
    
    {
        if ($n == 2) {
            return $n = 3;
        }
        $n += 2;
        while (! ($this->isPrime($n))) {
            $n += 2;
        }
        
        return $n;
    }

    public function genPrimeList($list)
    {
        while (array_sum($list) < $this->limit) {
            $list[] = $this->genNextPrime(array_values(array_slice($list, - 1))[0]);
        }
        array_pop($list);
        $this->primeList = $list;
        return;
    }

    public function isMatch()
    {
        if ($this->isPrime(array_sum($this->primeList))) {
            return TRUE;
        }
        return FALSE;
    }

    public function solver()
    {
        $list = $this->primeList;
        
        while (! ($this->isMatch())) {
            array_shift($list);
            $this->primeList = $list;
        }
        return;
    }
}

$p50 = new P50();
$p50->genPrimeList(array(2));
$p50->solver();
print_r($p50->primeList);
print_r(array_sum($p50->primeList));

?>