//
//  ParytListController.swift
//  UITable
//
//  Created by YuanZhan on 2/8/17.
//  Copyright © 2017 YuanZhan. All rights reserved.
//

import UIKit

class PartyListController: UITableViewController {
    
    var currentParty: NSMutableArray
    
    
    required init?(coder aDecoder: NSCoder) {
        self.currentParty = NSMutableArray()
        super.init(coder: aDecoder)
    }
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 2
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        switch (section) {
        case 0:
            return self.currentParty.count
        case 1:
            return 1
        default:
            return 0 }
    }
    
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        if(indexPath.section == 0) {
            let cell = tableView.dequeueReusableCell(withIdentifier: "MonsterCell", for: indexPath) as! MonsterCell
            let m: Monster = self.currentParty[indexPath.row] as! Monster
            cell.nameLabel.text = m.m_sName
            cell.attackLabel.text = "Attack Power: \(m.m_nLevel!)"
            
            switch m.m_sType {
            case "Grass":
                cell.attackLabel.textColor = UIColor.green
            case "Fire":
                cell.attackLabel.textColor = UIColor.red
            case "Water":
                cell.attackLabel.textColor = UIColor.blue
            case "Electric":
                cell.attackLabel.textColor = UIColor.orange
            case "Psychic":
                cell.attackLabel.textColor = UIColor.purple
            default:
                cell.attackLabel.textColor = UIColor.black
            }
            
            return cell
            
        }
        else {
            let cell = tableView.dequeueReusableCell(withIdentifier: "TotalCell", for: indexPath)
            cell.textLabel!.text = "Total Monster \(currentParty.count)"
            return cell
        }
    }
    
    // Override to support conditional editing of the table view.
    override func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool {
        if(indexPath.section == 0) {
            return true
        } else {
            return false
        }
    }
    
    
    // Override to support editing the table view.
    override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCellEditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            self.currentParty.removeObject(at: indexPath.row)
            tableView.deleteRows(at: [indexPath], with: .fade)
            let totalPath = NSIndexPath(row: 0, section: 1)
            tableView.reloadRows(at: [totalPath as IndexPath], with: .none)
        }
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "AddMonsterSegue"
        {
            let controller: AddMonsterController = segue.destination as! AddMonsterController
            controller.delegate = self as! AddMonsterDelegate
        }
    }
    
    func addMonster(monster: Monster) {
        self.currentParty.add(monster)
        self.tableView.reloadData()
    }
    
}
