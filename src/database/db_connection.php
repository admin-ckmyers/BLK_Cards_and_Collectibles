<?php
class Database {
    private static $db;

    public static function getConnection() {
        if (!self::$db) {
            self::$db = new SQLite3(__DIR__ . '/../blk_cards_collectibles.db');
        }
        return self::$db;
    }
}
?>
