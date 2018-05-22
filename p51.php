<?php

/*
 * Prime digit replacements
 *
 * Problem 51
 *
 * By replacing the 1st digit of the 2-digit number *3, it turns out that six of
 * the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
 *
 * By replacing the 3rd and 4th digits of 56**3 with the same digit, this
 * 5-digit number is the first example having seven primes among the ten
 * generated
 * numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
 * 56993. Consequently 56003, being the first member of this family, is the
 * smallest prime with this property.
 *
 * Find the smallest prime which, by replacing part of the number (not
 * necessarily adjacent digits) with the same digit, is part of an eight prime
 * value family.
 *
 * =============================================================================
 * Last digit cannot be *
 *
 * Create prime generating function (nextPrime). Approach answer from below i.e.
 * generate primes 10^2, check 'em (dubs) and go on.
 *
 */
class P51
{

    public $primeList;
    public function digits($n)
{
    return (int) (log10($n)) + 1;
}

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

    public function genPrimeList($list, $limit)
    {
        $currentPrime = array_values(array_slice($list, - 1))[0];
        while ($currentPrime < $limit) {
            $nextPrime = $this->genNextPrime($currentPrime);
            $list[] = $nextPrime;
            $currentPrime = $nextPrime;
        }
        array_pop($list);
        $this->primeList = $list;
        return;
    }
}

$p51 = new P51();
$p51->genPrimeList(array(101), 1000);
print_r($p51->primeList);

// O' Lordy, an insightful comment from Hades of Doom!

// print_r($p51->digits(100000));

?>