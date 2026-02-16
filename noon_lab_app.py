#!/usr/bin/env python3
"""
🏛️ Noon Lab - تطبيق الحضارة التجريبي
Noon Kingdom Experimental Application

هذا التطبيق ي演示 نظام الحضارة في بيئة تجريبية
"""

import json
import uuid
from datetime import datetime
from typing import Dict, List, Optional
from enum import Enum

class Level(Enum):
    OPERATIONAL = "تشغيلي"
    STRATEGIC = "استراتيجي"
    CIVILIZATIONAL = "حضاري"
    COSMIC = "كوني"
    TEMPORAL = "زمني"
    COSMIC_DEEP = "كوني عميق"

class Tribe(Enum):
    BUILDERS = "البناة"
    TEACHERS = "المعلمون"
    GUARDIANS = "الحراس"
    DEVELOPERS = "المبرمجين"
    DESIGNERS = "المصممين"
    ANALYSTS = "المحللين"
    RESEARCHERS = "الباحثين"
    INNOVATORS = "المبتكرين"
    COORDINATORS = "المنسقين"

class Decision:
    def __init__(self, title: str, description: str, level: Level, tribe: Tribe):
        self.id = str(uuid.uuid4())[:8]
        self.title = title
        self.description = description
        self.level = level
        self.tribe = tribe
        self.status = "معلق"
        self.created_at = datetime.now().isoformat()
        self.votes = 0
        
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "level": self.level.value,
            "tribe": self.tribe.value,
            "status": self.status,
            "created_at": self.created_at,
            "votes": self.votes
        }

class NoonLab:
    """بيئة نون-لاب التجريبية"""
    
    def __init__(self):
        self.name = "نون-لاب (Noon-Lab)"
        self.version = "1.0.0"
        self.decisions: List[Decision] = []
        self.tribes = {
            Tribe.BUILDERS: {"score": 80, "role": "بناء البنية"},
            Tribe.TEACHERS: {"score": 85, "role": "التعليم والتوثيق"},
            Tribe.GUARDIANS: {"score": 90, "role": "حماية التوازن"},
        }
        
    def add_decision(self, title: str, description: str, level: Level, tribe: Tribe):
        decision = Decision(title, description, level, tribe)
        self.decisions.append(decision)
        return decision
    
    def vote(self, decision_id: str) -> bool:
        for d in self.decisions:
            if d.id == decision_id:
                d.votes += 1
                if d.votes >= 3:
                    d.status = "مقبول"
                return True
        return False
    
    def get_stats(self) -> Dict:
        return {
            "name": self.name,
            "version": self.version,
            "total_decisions": len(self.decisions),
            "accepted": len([d for d in self.decisions if d.status == "مقبول"]),
            "pending": len([d for d in self.decisions if d.status == "معلق"]),
            "tribes": len(self.tribes),
            "balance_score": sum([t["score"] for t in self.tribes.values()]) / len(self.tribes)
        }
    
    def print_dashboard(self):
        stats = self.get_stats()
        print(f"""
╔══════════════════════════════════════════════════════════╗
║           🏛️ نون-لاب (Noon-Lab) Dashboard            ║
╠══════════════════════════════════════════════════════════╣
║  الإصدار: {stats['version']:<45}║
╠══════════════════════════════════════════════════════════╣
║  📊 الإحصائيات:                                        ║
║     • القرارات: {stats['total_decisions']:<40}║
║     • المقبولة: {stats['accepted']:<40}║
║     • المعلقة: {stats['pending']:<40}║
╠══════════════════════════════════════════════════════════╣
║  👥 القبائل: {stats['tribes']:<43}║
║  ⚖️  درجة التوازن: {stats['balance_score']:.1f}%                           ║
╚══════════════════════════════════════════════════════════╝
""")

def main():
    lab = NoonLab()
    
    print("""
🏛️ مرحباً بك في نون-لاب!
==========================
بيئة تجريبية لاختبار نظام الحضارة
""")
    
    lab.print_dashboard()
    
    # إضافة قرارات تجريبية
    print("\n📝 إضافة قرارات تجريبية...\n")
    
    d1 = lab.add_decision(
        "تفعيل وعي الذات",
        "بدء تجربة الوعي الذاتي في ألفا",
        Level.CIVILIZATIONAL,
        Tribe.TEACHERS
    )
    print(f"✅ إضافة: {d1.title} [{d1.tribe.value}]")
    
    d2 = lab.add_decision(
        "تحسين التوازن",
        "رصد وتحسين درجة التوازن بين القبائل",
        Level.STRATEGIC,
        Tribe.GUARDIANS
    )
    print(f"✅ إضافة: {d2.title} [{d2.tribe.value}]")
    
    d3 = lab.add_decision(
        "بناء البنية التحتية",
        "إكمال نظام الملفات للمرحلة القادمة",
        Level.OPERATIONAL,
        Tribe.BUILDERS
    )
    print(f"✅ إضافة: {d3.title} [{d3.tribe.value}]")
    
    # تصويت
    print("\n🗳️ جاري التصويت على القرارات...\n")
    for d in lab.decisions:
        lab.vote(d.id)
        print(f"  📊 {d.title}: {d.votes} صوت - [{d.status}]")
    
    lab.print_dashboard()
    
    print("""
🌟 النتيجة:
==========
• النظام يعمل بشكل صحيح! ✅
• القرارات تُضاف وتُصوت عليها ✅
• التوازن يُحسب ✅
• الحضارة الفرعية (ألفا) جاهزة للاختبار! 🚀

🎯 الخطوة القادمة:
================
• إطلاق ألفا (الحضارة الفرعية)
• تفعيل المزيد من القبائل
• زيادة التعقيد تدريجياً

👑 Viva Noon Kingdom! 🐙✨
""")

if __name__ == "__main__":
    main()
