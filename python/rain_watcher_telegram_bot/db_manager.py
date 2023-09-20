import sqlite3


class DBManager:

    def __init__(self, database):
        # Connecting to the database
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status=True):
        # Retrieving all the active subscribers
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ?", (status,)).fetchall()

    def add_subscriber(self, chat_id, notification_time, city, city_coordinates, user_language="en", status=True):
        # Adding a new subscriber
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `subscriptions` (`chat_id`, `notification_time`, `city`, `city_coordinates`, `user_language`, `status`) VALUES(?,?,?,?,?,?)",
                (chat_id, notification_time, city, city_coordinates, user_language, status))

    def update_user_language(self, chat_id, user_language="en"):
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `user_language` = ? WHERE `chat_id` = ?",
                                       (user_language, chat_id))

    def subscriber_does_exist(self, chat_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `subscriptions` WHERE `chat_id` = ?', (chat_id,)).fetchall()
            return bool(len(result))

    def update_subscription(self, chat_id, notification_time, city, city_coordinates, user_language, status=True):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `subscriptions` SET (`notification_time`, `city`, `city_coordinates`, `user_language`, `status`) = (?,?,?,?,?) WHERE `chat_id` = ?",
                (notification_time, city, city_coordinates, user_language, status, chat_id))

    def unsubscribe(self, chat_id):
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `chat_id` = ?", (False, chat_id))

    def close(self):
        self.connection.close()