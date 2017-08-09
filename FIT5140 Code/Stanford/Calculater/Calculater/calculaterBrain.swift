//
//  calculaterBrain.swift
//  Calculater
//
//  Created by YuanZhan on 6/8/17.
//  Copyright © 2017 Yuan Zhan. All rights reserved.
//

import Foundation

class CalculaterBrain {
    
    
    private var accumulator = 0.0
    
    
    func setOperand (operand: Double) {
        accumulator = operand
    }
    
    var operations: Dictionary<String, Operation> = [
        "π" : Operation.Constant(Double.pi),
        "e": Operation.Constant(M_E),
        "√": Operation.UnaryOperation(sqrt),
        "cos": Operation.UnaryOperation(cos)
    ]
    
    // new type , enum
    // cant inherit
    // pass by value --> like struct
    enum Operation{
        case Constant(Double)
        case UnaryOperation((Double) -> Double)
        case BinaryOperation
        case Equals
    }
    
    
    func performOperation (symbol: String){
        if let operation = operations[symbol] {
            switch operation {
            case .Constant(let value):
                accumulator = value
            case .UnaryOperation(let function):
                accumulator = function(accumulator)
            case .BinaryOperation:
                break
            case Operation.Equals:
                break
            }
        }
    }
    
    
    var result: Double {
        get{
            return accumulator
        }
    }
}
