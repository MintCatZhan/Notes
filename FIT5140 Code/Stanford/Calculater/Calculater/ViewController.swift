//
//  ViewController.swift
//  Calculater
//
//  Created by YuanZhan on 6/8/17.
//  Copyright © 2017 Yuan Zhan. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet private weak var display: UILabel!
    private var userIsInTheMiddleOfTyping = false
    
    private var brain =  CalculaterBrain()
    
    
    private var displayValue: Double {
        get {
            return Double(display.text!)!
        }
        
        set{
            display.text = String(newValue)
        }
    }
    
    
    
    @IBAction private func toughDigit(_ sender: UIButton) {
        let digit = sender.currentTitle!
        if userIsInTheMiddleOfTyping {
            let textCurrentlyInDisplay = display.text
            display!.text = textCurrentlyInDisplay! + digit
        } else {
            display!.text = digit
        }
        userIsInTheMiddleOfTyping = true
        
    }
    
    @IBAction private func performOperation(_ sender: UIButton) {
        if userIsInTheMiddleOfTyping {
            brain.setOperand(operand: displayValue)
            userIsInTheMiddleOfTyping = false
        }
        
        if let mathmaticalSymbol = sender.currentTitle {
            brain.performOperation(symbol: mathmaticalSymbol)
        }
        displayValue = brain.result
    }
    
}

