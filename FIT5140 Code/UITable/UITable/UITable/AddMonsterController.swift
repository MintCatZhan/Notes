//
//  AddMonsterController.swift
//  UITable
//
//  Created by YuanZhan on 2/8/17.
//  Copyright © 2017 YuanZhan. All rights reserved.
//

import UIKit

protocol AddMonsterDelegate {
    func addMonster(monster: Monster) }

class AddMonsterController: UITableViewController {
    var allMonsters = [Monster]()
    var delegate: AddMonsterDelegate?
    
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        var tempMonster = Monster(name: "Bulbasaur", type: "Grass", level: 100)
        allMonsters.append(tempMonster)
        tempMonster = Monster(name: "Charmander", type: "Fire", level: 150)
        allMonsters.append(tempMonster)
        tempMonster = Monster(name: "Squirtle", type: "Water", level: 130)
        allMonsters.append(tempMonster)
        tempMonster = Monster(name: "Pikachu", type: "Electric",level: 110)
        allMonsters.append(tempMonster)
        tempMonster = Monster(name: "Meowth", type: "Normal", level: 100)
        allMonsters.append(tempMonster)
        tempMonster = Monster(name: "Mewtwo", type: "Psychic", level: 450)
        allMonsters.append(tempMonster)
    }
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return self.allMonsters.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "MonsterCell", for: indexPath) as! MonsterCell
        let m: Monster = self.allMonsters[indexPath.row]
        cell.nameLabel.text = m.m_sName
        cell.attackLabel.text = "Attack Power: \(m.m_nLevel!)"
        switch m.m_sType {
        case "Grass":
            cell.attackLabel.textColor = UIColor.green
        case "Fire":
            cell.attackLabel.textColor = UIColor.red
        case "Water":
            cell.attackLabel.textColor = UIColor.blue
        case "Psychic":
            cell.attackLabel.textColor = UIColor.purple
        default:
            cell.attackLabel.textColor = UIColor.black
        }
        return cell
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let selectedMonster: Monster = self.allMonsters[indexPath.row]
        self.delegate!.addMonster(monster: selectedMonster)
        self.navigationController!.popViewController(animated: true)
    }
}
