export function getCondition(condition) {
    if (condition === 'Nytt') {
      return 'Nytt';
    } else if (condition === 'Använd_Nyskick') {
      return 'Använd Nyskick';
    } else if (condition === 'Använd_Gott_Skick') {
      return 'Använd Gott Skick';
    } else if (condition === 'Använd_Slitet_skick') {
      return 'Använd Slitet skick';
    }
  }