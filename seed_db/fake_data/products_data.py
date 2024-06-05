from . import *


def data(): 
    return [
    {
        'name': 'SonicWave Pro 500 Headphones',
        'image': 'sonicwave.png',
        'description': 'Latest model with A15 Bionic chip',
        'seller_id': 2,
        'buyer_id': None,
        'price': 799.0,
        'date': datetime(2024, 5, 4, 12, 34, 56, 789012),
        'condition': schemas.product.ConditionEnum.NEW,
        'category_id': 1,
    },
    {
        'name': 'BassBoost Ultra X2 Headphones',
        'image': 'bassboost.png',
        'description': 'High resolution',
        'seller_id': 1,
        'buyer_id': None,
        'price': 109.0,
        'date': datetime(2024, 5, 5, 12, 34, 56, 789012),
        'condition': schemas.product.ConditionEnum.USED,
        'category_id': 1,
    },
    {
        'name': 'Sony WH-1000XM4 Headphones',
        'image': 'sony_wh1000xm4.png',
        'description': 'Industry-leading noise cancellation',
        'seller_id': 4,
        'buyer_id': None,
        'price': 350.0,
        'date': datetime(2024, 5, 6, 12, 34, 56, 789012),
        'condition': schemas.product.ConditionEnum.NEW,
        'category_id': 1,
    },
    {
        'name': 'NoiseGuard Active 300',
        'image': 'dell_xps13.png',
        'description': 'Good headphones.',
        'seller_id': 3,
        'buyer_id': None,
        'price': 260.0,
        'date': datetime(2024, 5, 7, 12, 34, 56, 789012),
        'condition': schemas.product.ConditionEnum.USED,
        'category_id': 1,
    },
    {
        'name': 'Apple Watch Series 7',
        'image': 'apple_watch_series7.png',
        'description': 'Advanced health monitoring features',
        'seller_id': 6,
        'buyer_id': None,
        'price': 399.0,
        'date': datetime(2024, 5, 8, 12, 34, 56, 789012),
        'condition': schemas.product.ConditionEnum.NEW,
        'category_id': 1,
    },
    {
        'name': 'Canon EOS R5 Camera',
        'image': 'canon_eos_r5.png',
        'description': 'Full-frame mirrorless camera with 45MP sensor',
        'seller_id': 7,
        'buyer_id': None,
        'price': 3899.0,
        'date': datetime(2024, 5, 9, 12, 34, 56, 789012),
        'condition': schemas.product.ConditionEnum.USED,
        'category_id': 1,
    },
    {
        'name': 'PlayStation 5',
        'image': 'ps5.png',
        'description': 'Next-gen gaming console with ultra-high-speed SSD',
        'seller_id': 5,
        'buyer_id': None,
        'price': 499.0,
        'date': datetime(2024, 5, 10, 12, 34, 56, 789012),
        'condition': schemas.product.ConditionEnum.NEW,
        'category_id': 2,
    },
    {
        'name': 'Nikon Z6 II',
        'image': 'nikon_z6_ii.png',
        'description': 'Mirrorless camera with 24.5MP sensor and 4K video',
        'seller_id': 8,
        'buyer_id': None,
        'price': 1999.0,
        'date': datetime(2024, 5, 11, 12, 34, 56, 789012),
        'condition': schemas.product.ConditionEnum.USED,
        'category_id': 3,
    },
    {
        'name': 'Microsoft Surface Pro 7',
        'image': 'surface_pro7.png',
        'description': '2-in-1 laptop with Intel i5 processor',
        'seller_id': 9,
        'buyer_id': None,
        'price': 899.0,
        'date': datetime(2024, 5, 12, 12, 34, 56, 789012),
        'condition': schemas.product.ConditionEnum.NEW,
        'category_id': 4,
    },
    {
        'name': 'Bose QuietComfort 35 II',
        'image': 'bose_qc35ii.png',
        'description': 'Wireless noise-cancelling headphones',
        'seller_id': 10,
        'buyer_id': None,
        'price': 299.0,
        'date': datetime(2024, 5, 13, 12, 34, 56, 789012),
        'condition': schemas.product.ConditionEnum.USED,
        'category_id': 1,
    }
]