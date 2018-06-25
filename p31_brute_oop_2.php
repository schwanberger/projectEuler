<?php

/*
 * Project Euler problem 31: https://projecteuler.net/problem=31
 *
 * Problem description:
 * ===============================================================================================================
 * In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
 *
 * 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
 * It is possible to make £2 in the following way:
 *
 * 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
 * How many different ways can £2 be made using any number of coins?
 * ===============================================================================================================
 *
 * The solution below is a naïve algorithm which bruteforces the problem. Loose description:
 *
 * Given a set of possible coins, an array "A" with entries (200,100,50,20,10,5,2,1)
 * Given an array "B" with one entry, the entry being 200:
 * 1. Check if the sum of all elements of B <= 200, if so remove all 1's in the array and split last entry to the next largest as per A, new array is B'.
 * 2. Check if the sum of all elements of B' is 200 if not append B' with an entry equal to or immediately less than the last entry of B'
 * 3. Continue running down the list via a while loop and stop when B' contains two-hundred 1's. Before each split a counter is incremented;
 */
class P31
{
    public $coinSet = array(200,100,50,20,10,5,2,1);
    public $sum_max = 200;
    public $counter = 0;

    public function isValid(&$array)
    {
        if (array_sum($array) > $this->sum_max) {
            return (FALSE);
        }
        return (TRUE);
    }

    public function isComplete(&$array)
    {
        if (array_sum($array) == $this->sum_max) {
            return (TRUE);
        }
        return (FALSE);
    }

    public function &split(&$array)
    {
        $array = array_filter($array, function ($n) {
            return ($n > 1);
        });
        $element = array_search(end($array), $this->coinSet);
        $array[key($array)] = $this->coinSet[$element + 1];
        reset($array);
        return $array;
    }

    public function &addElement(&$array)
    {
        $array[] = end($array);
        return $array;
    }

    public function solver(&$array)
    {
        while (count($array) < $this->sum_max) {
            if ($this->isComplete($array)) {
                $this->counter ++;
                $array = $this->split($array);
            }
            if (! ($this->isValid($array))) {
                $array = $this->split($array);
            }
            if ($this->isValid($array) & ! ($this->isComplete($array))) {
                $array = $this->addElement($array);
            }
        }
        $this->counter ++;
        return (print_r($this->counter));
    }
}

$p31 = new P31();

$target = array($p31->sum_max = 200);
$p31->solver($target);

?>