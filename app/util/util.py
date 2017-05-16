from app.account.models import sites, User

sites_endpoint = {
    sites.CHEMISTRY: 'chemistry.index',
    sites.CHINESE_JUNIOR: 'chinese_junior.index',
    sites.CHINESE_SENIOR: 'chinese_senior.index',
    sites.ENGLISH_JUNIOR: 'english_junior.index',
    sites.ENGLISH_SENIOR: 'english_senior.index',
    sites.MATH_JUNIOR: 'math_junior.index',
    sites.MATH_SENIOR: 'math_senior.index',
    sites.PHYSICS_JUNIOR: 'physics_junior.index',
    sites.PHYSICS_SENIOR: 'physics_senior.index'
}

def redirect_sites(user):
    if user.sites > 0 and user.sites & (user.sites - 1) == 0:
        return sites_endpoint[user.sites]
    else:
        return 'main.index'
