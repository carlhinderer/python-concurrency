import random
import redis

def initial_inventory_load(r):
    random.seed(444)
    hats = {f"hat:{random.getrandbits(32)}": i for i in (
        {
            "color": "black",
            "price": 49.99,
            "style": "fitted",
            "quantity": 1000,
            "npurchased": 0,
        },
        {
            "color": "maroon",
            "price": 59.99,
            "style": "hipster",
            "quantity": 500,
            "npurchased": 0,
        },
        {
            "color": "green",
            "price": 99.99,
            "style": "baseball",
            "quantity": 200,
            "npurchased": 0,
        })
    }

    # Use the hash multi-set in a pipeline
    with r.pipeline() as pipe:
        for h_id, hat in hats.items():
            pipe.hmset(h_id, hat)
        pipe.execute()

    # Asynchronous save
    r.bgsave()


def get_db_info(r):
    # View all the keys in the db. Careful, this is O(n)!
    r.keys()


def purchase(r, k):
    # Here, we simulate what happens when a user clicks 'Purchase'
    r.hincrby("hat:56854717", "quantity", -1)
    r.hincrby("hat:56854717", "npurchased", 1)
    r.hincrby("hat:56854717", "npurchased", 1)


if __name__ == '__main__':
    r = redis.Redis(db=1)
    initial_inventory_load(r)
