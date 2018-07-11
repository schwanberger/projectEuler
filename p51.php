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
 * A1: Smallest prime, p1, of any family must be in some list of primes.
 * A2: A prime p1 can be written as an array where each element is a digit of
 * p1, ap1.
 * P1: p0 must have at least two digits which are the same. (determined by brute
 * force of single digit substituion)
 * T1: The resulting array of the subtraction of ap1 and any other family member
 * apx contains at least one zero
 * T2: array_unique on the resulting array of the subtraction of ap1 and any
 * other family member apx contains exactly two elements,
 * 0 as first elemeent and a negative number between -1 and -9
 *
 *
 */
class P51
{
    public $primeList;
    public $testList;
    public $testListList;
    public $digitPrimeList;
    public $candidateList;

    private function digits($n)
    {
        return (int) (log10($n)) + 1;
    }

    private function isPrime($n)
    {
        for ($x = 2; $x < 0.5 * $n; $x ++) {
            if ($n % $x == 0) {
                return FALSE;
            }
        }
        return TRUE;
    }

    private function genNextPrime($n)
    {
        $n += 1;
        while (! ($this->isPrime($n))) {
            $n += 1;
        }
        
        return $n;
    }

    public function genPrimeList($lowerlimit, $upperlimit)
    {
        $currentPrime = $lowerlimit;
        while ($currentPrime < $upperlimit) {
            $nextPrime = $this->genNextPrime($currentPrime);
            $list[] = $nextPrime;
            $currentPrime = $nextPrime;
        }
        array_pop($list);
        $this->primeList = $list;
        return;
    }

    public function find_p0_1sd()
    // Used to determine P1
    {
        for ($i = 0; $i < count($this->primeList); $i ++) {
            // for ($i = 0; $i < 2; $i ++) {
            $target = $this->primeList[$i];
            
            for ($j = 0; $j < $this->digits($target) - 1; $j ++) {
                if (substr($target, $j, 1) > 3) {
                    continue;
                }
                $this->testList[] = $target;
                
                for ($k = 1; $k <= 9 - substr($target, $j, 1); $k ++) {
                    $test = $target + $k * 10 ** ($this->digits($target) - 1 - $j);
                    if (in_array($test, $this->primeList)) {
                        
                        $this->testList[] = $test;
                    }
                }
                $this->testListList[] = $this->testList;
                $this->testList = array();
            }
        }
        
        return;
    }

    public function convertNumberToArrayofDigits($n)
    {
        $ArrayOfDigits = array();
        $numdigits = $this->digits($n);
        for ($i = 0; $i < $numdigits; $i ++) {
            $ArrayOfDigits[] = substr($n, $i, 1);
        }
        
        return $ArrayOfDigits;
    }

    public function createDigitPrimeList()
    {
        for ($i = 0; $i < count($this->primeList); $i ++) {
            $this->digitPrimeList[] = $this->convertNumberToArrayofDigits($this->primeList[$i]);
        }
        return;
    }

    public function subractArrayElements($ar1, $ar2)
    {
        $diff = array();
        foreach ($ar1 as $key => $value) {
            $diff[$key] = $ar2[$key] - $ar1[$key];
        }
        return $diff;
    }

    public function find_p0($familysize)
    {
        $tempList = array();
        for ($i = 0; $i < count($this->primeList); $i ++) {
            for ($j = 1; $j < count($this->primeList); $j ++) {
                $temp = $this->subractArrayElements($this->digitPrimeList[$i], $this->digitPrimeList[$j]);
                print_r($temp);
                rsort($temp);
                if ($temp[0] == 0 and count(array_unique($temp)) == 2) {
                    $tempList[] = $temp;
                }
            }
            if (count($tempList) == $familysize - 1) {
                $this->candidateList = $tempList;
                return;
            }
            $tempList = array();
        }
        return;
    }
}
$p51 = new P51();

$p51->genPrimeList(100, 1000);
$p51->createDigitPrimeList();
$p51->find_p0(5);
print_r($p51->candidateList);

// print_r($p51->digitPrimeList);
// print_r($p51->primeList);
// print_r($p51->subractArrayElements(array(1,1,3,1,3),array(1,1,2,1,2)));

// $p51->find_p0_1sd();
// print_r($p51->primeList);
// print_r($p51->testList);
// print_r($p51->primeList);
// $derp = array(0,- 1,0,0,- 1);
// rsort($derp);
// print_r($derp);
// print_r(array_unique($derp));

// array_multisort($p51->testListList);
// print_r($p51->testListList);
?>
